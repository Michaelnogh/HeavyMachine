import { useState } from 'react'
import styles from './ImageGallery.module.css'

export default function ImageGallery({ images, machineName }) {
  // Index of the currently displayed large image
  const [activeIndex, setActiveIndex] = useState(0)

  if (!images || images.length === 0) return null

  return (
    <div className={styles.gallery}>
      {/* Main large image */}
      <div className={styles.mainWrap}>
        <img
          src={images[activeIndex]}
          alt={`${machineName} — image ${activeIndex + 1}`}
          className={styles.mainImage}
        />
        {/* Counter badge */}
        <span className={styles.counter}>
          {activeIndex + 1} / {images.length}
        </span>
      </div>

      {/* Thumbnail strip */}
      <div className={styles.thumbs}>
        {images.map((src, i) => (
          <button
            key={i}
            className={`${styles.thumb} ${i === activeIndex ? styles.thumbActive : ''}`}
            onClick={() => setActiveIndex(i)}
            aria-label={`Show image ${i + 1}`}
          >
            <img src={src} alt={`Thumbnail ${i + 1}`} />
          </button>
        ))}
      </div>
    </div>
  )
}
