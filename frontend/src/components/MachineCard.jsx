import SafeImage from './SafeImage'
import styles from './MachineCard.module.css'

// A distinct badge colour for each category
const CATEGORY_COLOR = {
  Bulldozer:    '#e65c00',
  Excavator:    '#1565c0',
  Backhoe:      '#2e7d32',
  Bobcat:       '#6a1b9a',
  'Mini Bagger':'#00838f',
  Loader:       '#c62828',
  Crane:        '#37474f',
  Forklift:     '#f57f17',
  Grader:       '#4527a0',
  Roller:       '#558b2f',
  'Dump Truck': '#4e342e',
  'Skid Steer': '#00695c',
}

export default function MachineCard({ machine, onViewDetails, isFavorite, onToggleFavorite }) {
  const badgeColor = CATEGORY_COLOR[machine.category] ?? '#555'
  const thumbnail  = machine.images?.[0]

  return (
    <article className={styles.card}>
      {/* Image + category badge + favorite button */}
      <div className={styles.imageWrap}>
        <SafeImage
          src={thumbnail}
          alt={machine.name}
          className={styles.image}
          fallbackLabel={machine.name}
        />
        <span className={styles.categoryBadge} style={{ background: badgeColor }}>
          {machine.category}
        </span>
        <button
          className={`${styles.favBtn} ${isFavorite ? styles.favActive : ''}`}
          onClick={(e) => { e.stopPropagation(); onToggleFavorite?.(machine.id) }}
          aria-label={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
          aria-pressed={isFavorite}
          title={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
        >
          {isFavorite ? '♥' : '♡'}
        </button>
      </div>

      {/* Card body */}
      <div className={styles.body}>
        <div className={styles.topRow}>
          <span className={styles.manufacturer}>{machine.manufacturer}</span>
          <span className={styles.year}>{machine.year}</span>
        </div>

        <h3 className={styles.name}>{machine.name}</h3>
        <p className={styles.model}>{machine.model}</p>
        <p className={styles.description}>{machine.description}</p>

        {/* Two key specs */}
        <div className={styles.specs}>
          <div className={styles.spec}>
            <span className={styles.specLabel}>Horsepower</span>
            <span className={styles.specValue}>{machine.horsepower} HP</span>
          </div>
          <div className={styles.specDivider} />
          <div className={styles.spec}>
            <span className={styles.specLabel}>Weight</span>
            <span className={styles.specValue}>
              {machine.weight.toLocaleString()} kg
            </span>
          </div>
        </div>

        {/* Details button */}
        <button className={styles.detailsBtn} onClick={onViewDetails}>
          View Details
        </button>
      </div>
    </article>
  )
}
