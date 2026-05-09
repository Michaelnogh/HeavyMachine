from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from machines_data import MACHINES

app = FastAPI(title="HeavyMachine Catalog API")

# Allow all origins — Nginx sits in front on EC2 so the API is
# reachable from the same host. Wildcard keeps it open for any setup.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build sorted category list from the data once at startup
CATEGORIES = sorted({m["category"] for m in MACHINES})


# ── Health check ────────────────────────────────────────────────────────────
# Used by load-balancers / target groups so they stop reporting "Unhealthy".

@app.get("/")
def root():
    return {"status": "ok", "service": "heavymachine-api"}


@app.get("/health")
def health():
    return {"status": "ok", "machines": len(MACHINES)}


# ── API endpoints (paths and response shapes unchanged) ─────────────────────

@app.get("/api/machines")
def get_machines(category: str = "", search: str = ""):
    """
    Returns all machines.
    Optional query params:
      ?category=Bulldozer   – filter by category (case-insensitive)
      ?search=cat           – search by name or manufacturer (case-insensitive)
    Both params can be combined.
    """
    category = category.strip()
    search   = search.strip().lower()

    result = MACHINES

    if category:
        result = [m for m in result if m["category"].lower() == category.lower()]

    if search:
        result = [
            m for m in result
            if search in m["name"].lower() or search in m["manufacturer"].lower()
        ]

    return result


@app.get("/api/categories")
def get_categories():
    """Returns a sorted list of all machine categories."""
    return CATEGORIES


@app.get("/api/machines/{machine_id}")
def get_machine(machine_id: int):
    """Returns a single machine by its id."""
    for m in MACHINES:
        if m["id"] == machine_id:
            return m
    raise HTTPException(status_code=404, detail="Machine not found")


if __name__ == "__main__":
    # Direct `python3 main.py` still works — boots Uvicorn on the same port.
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
