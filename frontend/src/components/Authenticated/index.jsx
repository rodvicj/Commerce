import useClient from "../Client";
import Header from "../Header";
import Products from "../Products";

function Authenticated() {
  const { JWT } = useClient();

  return (
    <>
      <Header />
      <Products access_token={JWT.access_token} />
    </>
  );
}

export default Authenticated;
