import { useEffect, useState } from "react";

import api from "../api/axios";

import EntityForm from "../components/entities/EntityForm";

function EntitiesPage() {

  const [entities, setEntities] = useState([]);

  const loadEntities = () => {

    api.get("/entities")
      .then(res => {
        setEntities(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  };

  useEffect(() => {
    loadEntities();
  }, []);

  return (

    <div className="container mt-5">

      <div className="d-flex justify-content-between mb-4">

        <h2>
          Entidades
        </h2>

        <button
          className="btn btn-success"
          data-bs-toggle="modal"
          data-bs-target="#entityModal"
        >
          + Añadir Entidad
        </button>

      </div>

      {/* TABLE */}
      <div className="card shadow">

        <div className="card-body">

          <div className="table-responsive">

            <table className="table table-striped table-bordered">

              <thead className="table-dark">

                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Sigla</th>
                  <th>Email</th>
                  <th>Teléfono</th>
                  <th>Centralizada</th>
                  <th>Activa</th>
                </tr>

              </thead>

              <tbody>

                {entities.map(entity => (

                  <tr key={entity.id}>

                    <td>{entity.id}</td>

                    <td>{entity.name}</td>

                    <td>{entity.short_name || "-"}</td>

                    <td>{entity.email || "-"}</td>

                    <td>{entity.phone || "-"}</td>

                    <td>

                      {entity.is_centralized ? (
                        <span className="badge bg-success">
                          Sí
                        </span>
                      ) : (
                        <span className="badge bg-secondary">
                          No
                        </span>
                      )}

                    </td>

                    <td>

                      {entity.is_active ? (
                        <span className="badge bg-success">
                          Activa
                        </span>
                      ) : (
                        <span className="badge bg-danger">
                          Inactiva
                        </span>
                      )}

                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

      {/* MODAL */}
      <div
        className="modal fade"
        id="entityModal"
        tabIndex="-1"
      >

        <div className="modal-dialog modal-xl">

          <div className="modal-content">

            <div className="modal-header">

              <h5 className="modal-title">
                Nueva Entidad
              </h5>

              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
              />

            </div>

            <div className="modal-body">

              <EntityForm onCreated={loadEntities} />

            </div>

          </div>

        </div>

      </div>

    </div>
    
  );
}

export default EntitiesPage;