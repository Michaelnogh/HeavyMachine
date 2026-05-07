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

export default function MachineCard({ machine, onViewDetails }) {
  const badgeColor = CATEGORY_COLOR[machine.category] ?? '#555'
  // Use the first image as the card thumbnail
  const thumbnail = machine.images?.[0] ?? 'https://placehold.co/400x260/ccc/555?text=No+Image'

  return (
    <article className={styles.card}>
      {/* Image + category badge */}
      <div className={styles.imageWrap}>
        <img
          src={thumbnail}
          alt={machine.name}
          className={styles.image}
          loading="lazy"
        />
        <span className={styles.categoryBadge} style={{ background: badgeColor }}>
          {machine.category}
        </span>
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
