import { useState } from 'react'
import SafeImage from './SafeImage'
import styles from './ImageGallery.module.css'

export default function ImageGallery({ images, machineName }) {
  // Index of the currently displayed large image
  const [activeIndex, setActiveIndex] = useState(0)

  if (!images || images.length === 0) return null

  return (
    <div className={styles.gallery}>
      {/* Main large image */}
      <div className={styles.mainWrap}>
        <SafeImage
          src={images[activeIndex]}
          alt={`${machineName} — image ${activeIndex + 1}`}
          className={styles.mainImage}
          fallbackLabel={machineName}
          loading="eager"
        />
        {/* Counter badge */}
        <span className={styles.counter}>
          {activeIndex + 1} / {images.length}
        </span>
      </div>

      {/* Thumbnail strip */}
      {images.length > 1 && (
        <div className={styles.thumbs}>
          {images.map((src, i) => (
            <button
              key={i}
              className={`${styles.thumb} ${i === activeIndex ? styles.thumbActive : ''}`}
              onClick={() => setActiveIndex(i)}
              aria-label={`Show image ${i + 1}`}
            >
              <SafeImage
                src={src}
                alt={`${machineName} thumbnail ${i + 1}`}
                fallbackLabel={machineName}
              />
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
