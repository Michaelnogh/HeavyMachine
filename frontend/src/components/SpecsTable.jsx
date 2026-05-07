import styles from './SpecsTable.module.css'

// Renders the technicalSpecs object as a clean two-column table
export default function SpecsTable({ specs }) {
  if (!specs || Object.keys(specs).length === 0) return null

  const rows = Object.entries(specs)

  return (
    <table className={styles.table}>
      <tbody>
        {rows.map(([label, value], i) => (
          <tr key={label} className={i % 2 === 0 ? styles.even : styles.odd}>
            <td className={styles.label}>{label}</td>
            <td className={styles.value}>{value}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
