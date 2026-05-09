import { useState, useEffect } from 'react'

/**
 * <img> wrapper that shows a styled SVG placeholder if the source fails.
 * Used everywhere we display a remote image so a broken URL never produces
 * a browser-default broken-image icon.
 */

// Inline SVG placeholder. Encoded as a data URI so it works offline and
// never makes a network request. Looks like a dark grey "image not available"
// card with a small camera-style icon.
function buildPlaceholder(label = 'Image unavailable') {
  const safe = (label || '').replace(/[<>&]/g, '')
  const svg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a2a2a"/>
      <stop offset="100%" stop-color="#1a1a1a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#g)"/>
  <g transform="translate(400 220)" fill="none" stroke="#F4A820" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    <rect x="-70" y="-50" width="140" height="100" rx="10"/>
    <circle cx="0" cy="5" r="28"/>
    <circle cx="45" cy="-32" r="6" fill="#F4A820"/>
  </g>
  <text x="400" y="340" text-anchor="middle" fill="#bbb"
        font-family="system-ui, sans-serif" font-size="22" font-weight="600">${safe}</text>
  <text x="400" y="370" text-anchor="middle" fill="#666"
        font-family="system-ui, sans-serif" font-size="14">image unavailable</text>
</svg>`.trim()
  return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`
}

export default function SafeImage({ src, alt, className, fallbackLabel, loading = 'lazy' }) {
  const [errored, setErrored] = useState(false)

  // Reset error state when src changes (e.g. user switches gallery thumbnail)
  useEffect(() => { setErrored(false) }, [src])

  const placeholder = buildPlaceholder(fallbackLabel || alt)
  const finalSrc = !src || errored ? placeholder : src

  return (
    <img
      src={finalSrc}
      alt={alt}
      className={className}
      loading={loading}
      onError={() => setErrored(true)}
    />
  )
}
