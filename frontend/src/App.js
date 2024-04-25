import { useJWTToken, Login } from "./components/Login";
import { Products } from "./components/Products";

function App() {
  const [JWT, setJWT] = useJWTToken();

  return (
    <div className="App">
      <Login />
      {JWT && <Products access_token={JWT.access_token} />}
    </div>
  );
}

export default App;
