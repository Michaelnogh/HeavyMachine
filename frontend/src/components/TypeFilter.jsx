import styles from './TypeFilter.module.css'

const TYPE_ICONS = {
  Bulldozer: '🚧',
  Excavator: '🏗',
  Backhoe: '⛏',
}

export default function TypeFilter({ types, selected, onChange, total }) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.inner}>
        <div className={styles.left}>
          <h2 className={styles.heading}>Browse by Type</h2>
          <span className={styles.count}>{total} machine{total !== 1 ? 's' : ''} found</span>
        </div>
        <div className={styles.pills}>
          <button
            className={`${styles.pill} ${selected === null ? styles.active : ''}`}
            onClick={() => onChange(null)}
          >
            All
          </button>
          {types.map((type) => (
            <button
              key={type}
              className={`${styles.pill} ${selected === type ? styles.active : ''}`}
              onClick={() => onChange(type)}
            >
              <span>{TYPE_ICONS[type] ?? '🔧'}</span>
              {type}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
