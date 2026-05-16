import { useState } from "react";
import api from "../../api/axios";

function EntityForm({ onCreated }) {
  const [formData, setFormData] = useState({
    name: "",
    short_name: "",
    nit: "",
    email: "",
    phone: "",
    address: "",
    acto_administrativo: "",
    separator: "-",
    is_centralized: false,
    central_dependency_code: "",
    representante_legal_nombre: "",
    representante_legal_cargo: "",
    nom_responsable_gestion_documental: "",
    cgo_responsable_gestion_documental: "",
    dep_responsable_gestion_documental: "",
    functions: "",
    logo_path: "",
    is_active: true,
  });

  const [logoPreview, setLogoPreview] = useState(null);
  const [logoFile, setLogoFile] = useState(null);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handlePaste = (e) => {
    const items = e.clipboardData.items;

    for (let item of items) {
      if (item.type.indexOf("image") !== -1) {
        const blob = item.getAsFile();

        setLogoFile(blob);

        const imageUrl = URL.createObjectURL(blob);

        setLogoPreview(imageUrl);

        break;
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const submitData = new FormData();

      Object.keys(formData).forEach((key) => {
        submitData.append(key, formData[key]);
      });

      if (logoFile) {
        submitData.append("logo", logoFile);
      }

      await api.post("/entities", submitData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("Entidad creada");

      if (onCreated) {
        onCreated();
      }
    } catch (err) {
      console.error(err);
      alert("Error");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="row g-3">
        <div className="col-md-6">
          <label>Nombre</label>

          <input
            className="form-control"
            name="name"
            required
            value={formData.name}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-3">
          <label>Sigla</label>

          <input
            className="form-control"
            name="short_name"
            value={formData.short_name}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-3">
          <label>NIT</label>

          <input
            className="form-control"
            name="nit"
            value={formData.nit}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-6">
          <label>Email</label>

          <input
            className="form-control"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-6">
          <label>Teléfono</label>

          <input
            className="form-control"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-12">
          <label>Dirección</label>

          <input
            className="form-control"
            name="address"
            value={formData.address}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-6">
          <label>Marco Regulatorio</label>

          <input
            className="form-control"
            name="acto_administrativo"
            value={formData.acto_administrativo}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-2">
          <label>Separador</label>

          <input
            className="form-control"
            name="separator"
            maxLength="1"
            value={formData.separator}
            onChange={handleChange}
          />
        </div>

        <div className="col-md-4 mt-4">
          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              name="is_centralized"
              checked={formData.is_centralized}
              onChange={handleChange}
            />

            <label className="form-check-label">Entidad Centralizada</label>
          </div>
        </div>
        <div className="col-md-12">
          <label className="form-label">Logo</label>

          <div
            className="border rounded p-4 bg-light text-center"
            onPaste={handlePaste}
            tabIndex="0"
            style={{
              minHeight: "200px",
              outline: "none",
            }}
          >
            <p>Haga click aquí y pegue la imagen con CTRL + V</p>

            {logoPreview && (
              <img
                src={logoPreview}
                alt="logo"
                style={{
                  maxWidth: "250px",
                  maxHeight: "180px",
                  objectFit: "contain",
                }}
              />
            )}
          </div>
        </div>
        <div className="col-md-12">
          <label>Funciones</label>

          <textarea
            className="form-control"
            rows="4"
            name="functions"
            value={formData.functions}
            onChange={handleChange}
          />
        </div>
      </div>

      <div className="mt-4 text-end">
        <button className="btn btn-success">Guardar</button>
      </div>
    </form>
  );
}

export default EntityForm;
