import { useEffect, useState } from 'react'
import Header from './components/Header'
import CategoryFilter from './components/CategoryFilter'
import SearchBar from './components/SearchBar'
import MachineCard from './components/MachineCard'
import MachineDetails from './components/MachineDetails'
import styles from './App.module.css'

const API = '/api'

export default function App() {
  // All machines fetched once from the API
  const [allMachines, setAllMachines]       = useState([])
  const [categories, setCategories]         = useState([])
  const [loading, setLoading]               = useState(true)
  const [error, setError]                   = useState(null)

  // Filter / search state (all handled client-side for simplicity)
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [searchQuery, setSearchQuery]           = useState('')

  // The machine currently open in the details modal (null = closed)
  const [selectedMachine, setSelectedMachine]   = useState(null)

  // Fetch categories list
  useEffect(() => {
    fetch(`${API}/categories`)
      .then((r) => r.json())
      .then(setCategories)
      .catch(() => {})
  }, [])

  // Fetch all machines once on mount
  useEffect(() => {
    setLoading(true)
    setError(null)
    fetch(`${API}/machines`)
      .then((r) => {
        if (!r.ok) throw new Error('Failed to fetch machines')
        return r.json()
      })
      .then((data) => {
        setAllMachines(data)
        setLoading(false)
      })
      .catch((e) => {
        setError(e.message)
        setLoading(false)
      })
  }, [])

  // Client-side filtering: apply category filter then search query
  const visibleMachines = allMachines
    .filter((m) => !selectedCategory || m.category === selectedCategory)
    .filter((m) => {
      if (!searchQuery.trim()) return true
      const q = searchQuery.toLowerCase()
      return (
        m.name.toLowerCase().includes(q) ||
        m.manufacturer.toLowerCase().includes(q)
      )
    })

  return (
    <div className={styles.app}>
      <Header />

      {/* Category filter bar */}
      <CategoryFilter
        categories={categories}
        selected={selectedCategory}
        onChange={setSelectedCategory}
        total={visibleMachines.length}
      />

      <main className={styles.main}>
        {/* Search bar */}
        <SearchBar value={searchQuery} onChange={setSearchQuery} />

        {/* Loading spinner */}
        {loading && (
          <div className={styles.center}>
            <div className={styles.spinner} />
            <p>Loading machinery catalog...</p>
          </div>
        )}

        {/* Connection error */}
        {error && (
          <div className={styles.error}>
            <span>⚠</span>
            <div>
              <strong>Could not connect to the API</strong>
              <p>Make sure the Python backend is running on port 8000.</p>
              <code>cd backend &amp;&amp; python main.py</code>
            </div>
          </div>
        )}

        {/* Empty state */}
        {!loading && !error && visibleMachines.length === 0 && (
          <div className={styles.center}>
            <p>No machines match your search.</p>
            <button
              className={styles.clearBtn}
              onClick={() => { setSelectedCategory(null); setSearchQuery('') }}
            >
              Clear filters
            </button>
          </div>
        )}

        {/* Machine grid */}
        {!loading && !error && visibleMachines.length > 0 && (
          <div className={styles.grid}>
            {visibleMachines.map((m) => (
              <MachineCard
                key={m.id}
                machine={m}
                onViewDetails={() => setSelectedMachine(m)}
              />
            ))}
          </div>
        )}
      </main>

      <footer className={styles.footer}>
        <p>© 2026 HeavyMachine Lab · Heavy Engineering Equipment Reference Catalog</p>
      </footer>

      {/* Details modal — only rendered when a machine is selected */}
      {selectedMachine && (
        <MachineDetails
          machine={selectedMachine}
          onClose={() => setSelectedMachine(null)}
        />
      )}
    </div>
  )
}
