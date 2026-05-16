
function App() {
  const [documents, setDocuments] = useState([])

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/api/documents')
      .then((response) => {
        setDocuments(response.data)
      })
  }, [])

  return (
    <div>
      <h1>Documents</h1>

      {documents.map((doc) => (
        <div key={doc.id}>
          {doc.title}
        </div>
      ))}
    </div>
  )
}

export default App