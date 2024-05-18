import { useClient } from "./Client";
import { Products } from "./Products";

function Authenticated() {
  const { JWT, logout, user } = useClient();

  return (
    <>
      <p>{user?.username}</p>
      <button onClick={() => logout()}>Logout</button>
      <Products access_token={JWT.access_token} />
    </>
  );
}

export default Authenticated;
