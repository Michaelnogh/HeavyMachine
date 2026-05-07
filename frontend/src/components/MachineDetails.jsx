import { useEffect } from 'react'
import ImageGallery from './ImageGallery'
import SpecsTable from './SpecsTable'
import styles from './MachineDetails.module.css'

export default function MachineDetails({ machine, onClose }) {
  // Close modal when Escape key is pressed
  useEffect(() => {
    const handleKey = (e) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', handleKey)
    return () => window.removeEventListener('keydown', handleKey)
  }, [onClose])

  // Prevent body scroll while modal is open
  useEffect(() => {
    document.body.style.overflow = 'hidden'
    return () => { document.body.style.overflow = '' }
  }, [])

  return (
    /* Clicking the dark overlay closes the modal */
    <div className={styles.overlay} onClick={onClose}>
      {/* Stop click propagation so clicking inside the panel doesn't close */}
      <div className={styles.panel} onClick={(e) => e.stopPropagation()}>

        {/* ── Header ── */}
        <div className={styles.header}>
          <div className={styles.headerInfo}>
            <span className={styles.manufacturer}>{machine.manufacturer}</span>
            <h2 className={styles.name}>{machine.name}</h2>
            <span className={styles.meta}>
              {machine.model} · {machine.year} · {machine.category}
            </span>
          </div>
          <button className={styles.closeBtn} onClick={onClose} aria-label="Close">
            ✕
          </button>
        </div>

        {/* ── Scrollable content ── */}
        <div className={styles.content}>

          {/* Image gallery */}
          <ImageGallery images={machine.images} machineName={machine.name} />

          {/* Description */}
          <section className={styles.section}>
            <h3 className={styles.sectionTitle}>Description</h3>
            <p className={styles.description}>{machine.description}</p>
          </section>

          {/* Quick stats row */}
          <div className={styles.statsRow}>
            <div className={styles.stat}>
              <span className={styles.statLabel}>Horsepower</span>
              <span className={styles.statValue}>{machine.horsepower} HP</span>
            </div>
            <div className={styles.stat}>
              <span className={styles.statLabel}>Operating Weight</span>
              <span className={styles.statValue}>{machine.weight.toLocaleString()} kg</span>
            </div>
            <div className={styles.stat}>
              <span className={styles.statLabel}>Model Year</span>
              <span className={styles.statValue}>{machine.year}</span>
            </div>
            <div className={styles.stat}>
              <span className={styles.statLabel}>Category</span>
              <span className={styles.statValue}>{machine.category}</span>
            </div>
          </div>

          {/* Technical specifications */}
          <section className={styles.section}>
            <h3 className={styles.sectionTitle}>Technical Specifications</h3>
            <SpecsTable specs={machine.technicalSpecs} />
          </section>

          {/* Schematics */}
          {machine.schematics && machine.schematics.length > 0 && (
            <section className={styles.section}>
              <h3 className={styles.sectionTitle}>Schematics</h3>
              <div className={styles.schematics}>
                {machine.schematics.map((src, i) => (
                  <div key={i} className={styles.schematicWrap}>
                    <img
                      src={src}
                      alt={`${machine.name} schematic ${i + 1}`}
                      className={styles.schematicImg}
                    />
                    <span className={styles.schematicLabel}>
                      {i === 0 ? 'Side Profile' : 'Dimensions'}
                    </span>
                  </div>
                ))}
              </div>
            </section>
          )}

        </div>
      </div>
    </div>
  )
}
