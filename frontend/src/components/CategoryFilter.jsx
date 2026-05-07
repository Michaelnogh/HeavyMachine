import styles from './CategoryFilter.module.css'

// Emoji icon for each category — fallback to wrench for unknown types
const CATEGORY_ICONS = {
  Bulldozer:   '🚧',
  Excavator:   '🏗',
  Backhoe:     '⛏',
  Bobcat:      '🐾',
  'Mini Bagger':'🔩',
  Loader:      '🪣',
  Crane:       '🏚',
  Forklift:    '🔱',
  Grader:      '🛣',
  Roller:      '🔘',
  'Dump Truck':'🚛',
  'Skid Steer':'⚙',
}

export default function CategoryFilter({ categories, selected, onChange, total }) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.inner}>
        <div className={styles.left}>
          <h2 className={styles.heading}>Browse by Category</h2>
          <span className={styles.count}>
            {total} machine{total !== 1 ? 's' : ''} found
          </span>
        </div>

        <div className={styles.pills}>
          {/* "All" pill resets the filter */}
          <button
            className={`${styles.pill} ${selected === null ? styles.active : ''}`}
            onClick={() => onChange(null)}
          >
            All
          </button>

          {categories.map((cat) => (
            <button
              key={cat}
              className={`${styles.pill} ${selected === cat ? styles.active : ''}`}
              onClick={() => onChange(cat)}
            >
              <span className={styles.icon}>{CATEGORY_ICONS[cat] ?? '🔧'}</span>
              {cat}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
