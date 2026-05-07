import styles from './Header.module.css'

export default function Header() {
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
        <div className={styles.brand}>
          <span className={styles.brandBadge}>Caterpillar</span>
          <span className={styles.brandSub}>Authorized Dealer Reference</span>
        </div>
      </div>
    </header>
  )
}
