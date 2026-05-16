import { useEffect, useState } from "react";

export default function EntitiesPage() {
  const [entities, setEntities] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    description: "",
  });
  const [editingId, setEditingId] = useState(null);

  const API_URL = "http://127.0.0.1:5000/entities";

  useEffect(() => {
    fetchEntities();
  }, []);

  const fetchEntities = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setEntities(data);
    } catch (error) {
      console.error("Error fetching entities:", error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (editingId) {
        await fetch(`${API_URL}/${editingId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        });
      } else {
        await fetch(API_URL, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        });
      }

      setFormData({
        name: "",
        description: "",
      });

      setEditingId(null);
      fetchEntities();
    } catch (error) {
      console.error("Error saving entity:", error);
    }
  };

  const handleEdit = (entity) => {
    setFormData({
      name: entity.name,
      description: entity.description,
    });

    setEditingId(entity.id);
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`${API_URL}/${id}`, {
        method: "DELETE",
      });

      fetchEntities();
    } catch (error) {
      console.error("Error deleting entity:", error);
    }
  };

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>Entities Management</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: "30px" }}>
        <div style={{ marginBottom: "10px" }}>
          <input
            type="text"
            name="name"
            placeholder="Entity Name"
            value={formData.name}
            onChange={handleChange}
            required
            style={{
              width: "100%",
              padding: "10px",
              fontSize: "16px",
            }}
          />
        </div>

        <div style={{ marginBottom: "10px" }}>
          <textarea
            name="description"
            placeholder="Entity Description"
            value={formData.description}
            onChange={handleChange}
            required
            rows="4"
            style={{
              width: "100%",
              padding: "10px",
              fontSize: "16px",
            }}
          />
        </div>

        <button
          type="submit"
          style={{
            padding: "10px 20px",
            fontSize: "16px",
            cursor: "pointer",
          }}
        >
          {editingId ? "Update Entity" : "Create Entity"}
        </button>
      </form>

      <h2>Entities List</h2>

      {entities.length === 0 ? (
        <p>No entities found.</p>
      ) : (
        <table
          border="1"
          cellPadding="10"
          cellSpacing="0"
          width="100%"
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {entities.map((entity) => (
              <tr key={entity.id}>
                <td>{entity.id}</td>
                <td>{entity.name}</td>
                <td>{entity.description}</td>

                <td>
                  <button
                    onClick={() => handleEdit(entity)}
                    style={{
                      marginRight: "10px",
                      cursor: "pointer",
                    }}
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(entity.id)}
                    style={{
                      cursor: "pointer",
                    }}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}