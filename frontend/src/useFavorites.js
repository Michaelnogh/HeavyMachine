import { useEffect, useState, useCallback } from 'react'

const STORAGE_KEY = 'heavymachine:favorites'

// Read the stored set once at startup. Wrapped in try/catch because
// localStorage can throw in private-browsing or when JSON is corrupted.
function readInitial() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw)
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

/**
 * Hook for tracking favorited machine IDs.
 *   const { favorites, isFavorite, toggleFavorite, count } = useFavorites()
 *
 * Persists to localStorage on every change and syncs across tabs via the
 * native `storage` event so opening the catalog in two windows stays consistent.
 */
export default function useFavorites() {
  const [favorites, setFavorites] = useState(readInitial)

  // Persist on change
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites))
    } catch { /* ignore quota / private mode errors */ }
  }, [favorites])

  // Sync between tabs
  useEffect(() => {
    const onStorage = (e) => {
      if (e.key !== STORAGE_KEY) return
      try {
        const next = e.newValue ? JSON.parse(e.newValue) : []
        if (Array.isArray(next)) setFavorites(next)
      } catch { /* ignore */ }
    }
    window.addEventListener('storage', onStorage)
    return () => window.removeEventListener('storage', onStorage)
  }, [])

  const isFavorite = useCallback(
    (id) => favorites.includes(id),
    [favorites],
  )

  const toggleFavorite = useCallback((id) => {
    setFavorites((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id],
    )
  }, [])

  return {
    favorites,
    isFavorite,
    toggleFavorite,
    count: favorites.length,
  }
}
