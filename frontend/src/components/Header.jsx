import styles from './Header.module.css'

export default function Header({ favoritesCount = 0, showFavoritesOnly = false, onToggleFavorites }) {
  return (
    <header className={styles.header}>
      <div className={styles.inner}>
        <div className={styles.logo}>
          <span className={styles.logoIcon}>⚙</span>
          <div>
            <span className={styles.logoTitle}>HeavyMachine</span>
            <span className={styles.logoSub}>Equipment Catalog</span>
          </div>
        </div>

        <div className={styles.actions}>
          <button
            className={`${styles.favToggle} ${showFavoritesOnly ? styles.favToggleActive : ''}`}
            onClick={onToggleFavorites}
            aria-pressed={showFavoritesOnly}
            title={showFavoritesOnly ? 'Show all machines' : 'Show only favorites'}
          >
            <span className={styles.favIcon}>{showFavoritesOnly ? '♥' : '♡'}</span>
            <span className={styles.favLabel}>Favorites</span>
            <span className={styles.favCount}>{favoritesCount}</span>
          </button>

          <div className={styles.brand}>
            <span className={styles.brandBadge}>Caterpillar</span>
            <span className={styles.brandSub}>Authorized Dealer Reference</span>
          </div>
        </div>
      </div>
    </header>
  )
}
