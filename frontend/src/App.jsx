import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import entitiesPage from "./pages/entitiesPage";

function HomePage() {

  return (
    <div className="container py-5 text-center">

      <h2>Bienvenidos!</h2>

      <p>
        Seleccione opción en el menú superior
      </p>

    </div>
  );
}

function Placeholder({ title }) {

  return (
    <div className="container mt-5">

      <h2>{title}</h2>

      <div className="alert alert-info mt-4">
        Module migration pending
      </div>

    </div>
  );
}

function App() {

  return (

    <BrowserRouter>

      {/* NAVBAR */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4">

        <div className="container-fluid">

          <Link
            className="navbar-brand fw-bold"
            to="/"
          >
            Generador de Tablas de Retención Documental - TRD
          </Link>

          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
          >
            <span className="navbar-toggler-icon"></span>
          </button>

          <div
            className="collapse navbar-collapse"
            id="navbarNav"
          >

            <ul className="navbar-nav me-auto">

              {/* TABLAS */}
              <li className="nav-item dropdown">

                <a
                  className="nav-link dropdown-toggle"
                  href="#"
                  role="button"
                  data-bs-toggle="dropdown"
                >
                  Tablas
                </a>

                <ul className="dropdown-menu">

                  <li>
                    <Link
                      className="dropdown-item"
                      to="/entities"
                    >
                      Entidades
                    </Link>
                  </li>

                  <li>
                    <Link
                      className="dropdown-item"
                      to="/dependencies"
                    >
                      Dependencias
                    </Link>
                  </li>

                  <li>
                    <Link
                      className="dropdown-item"
                      to="/series"
                    >
                      Series
                    </Link>
                  </li>

                  <li>
                    <Link
                      className="dropdown-item"
                      to="/subseries"
                    >
                      Subseries
                    </Link>
                  </li>

                  <li>
                    <Link
                      className="dropdown-item"
                      to="/doctypes"
                    >
                      Tipos documentales
                    </Link>
                  </li>

                </ul>

              </li>

              {/* GENERADOR */}
              <li className="nav-item">

                <Link
                  className="nav-link"
                  to="/generator"
                >
                  Generador de códigos documentales
                </Link>

              </li>

              {/* STUDIES */}
              <li className="nav-item">

                <Link
                  className="nav-link"
                  to="/documental-studies"
                >
                  Estudios documentales
                </Link>

              </li>

            </ul>

          </div>

        </div>

      </nav>

      {/* ROUTES */}
      <Routes>

        <Route
          path="/"
          element={<HomePage />}
        />

        <Route
          path="/entities"
          element={<entitiesPage />}
        />

        <Route
          path="/dependencies"
          element={<Placeholder title="Dependencias" />}
        />

        <Route
          path="/series"
          element={<Placeholder title="Series" />}
        />

        <Route
          path="/subseries"
          element={<Placeholder title="Subseries" />}
        />

        <Route
          path="/doctypes"
          element={<Placeholder title="Tipos documentales" />}
        />

        <Route
          path="/generator"
          element={<Placeholder title="Generador documental" />}
        />

        <Route
          path="/documental-studies"
          element={<Placeholder title="Estudios documentales" />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;