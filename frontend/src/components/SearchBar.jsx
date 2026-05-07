import styles from './SearchBar.module.css'

export default function SearchBar({ value, onChange }) {
  return (
    <div className={styles.wrapper}>
      <span className={styles.icon}>🔍</span>
      <input
        className={styles.input}
        type="search"
        placeholder="Search by machine name or manufacturer…"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        aria-label="Search machines"
      />
      {/* Show a clear button only when there is text */}
      {value && (
        <button
          className={styles.clearBtn}
          onClick={() => onChange('')}
          aria-label="Clear search"
        >
          ✕
        </button>
      )}
    </div>
  )
}
