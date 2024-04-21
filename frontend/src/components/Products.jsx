import React, { useState, useEffect } from "react";
import { getJWTToken } from "./Login";

export const Products = ({ name }) => {
  // const [JWT, setJWT] = useJWTToken();
  const count = React.useRef(0);
  const [products, setProducts] = useState([]);
  const [JWT, setJWT] =  useState(getJWTToken());

  const getToken = () => {
    setJWT(getJWTToken())
    console.log("JWT", JWT);
    return;
  };

  useEffect(() => {
    const fetchData = async () => {
      if (JWT) {
        try {
          const response = await fetch("http://127.0.0.1:8000/api/products", {
            headers: {
              Authorization: `Bearer ${JWT.access_token}`,
            },
          });
          console.log("response", response);
          // const response = await fetch("http://127.0.0.1:8000/api/products");
          if (response.status === 200) {
            const data = await response.json();
            setProducts(data.results);
          }
        } catch (error) {
          console.log("error:", error);
        }
        console.log("JWT inside useEffect", JWT);
      }
    };

    fetchData();
    count.current = count.current + 1;
    console.log("products", products);
  }, [JWT]);

  return (
    <div>
      <button onClick={() => getToken()}>getToken</button>
      <p>Hello {name}</p>
      {products?.map((item, index) => {
        return (
          <div key={index}>
            <p>{item.name}</p>
            <img src={item.image} alt="item.name" />
          </div>
        );
      })}
      <h1>Render Count: {count.current}</h1>
    </div>
  );
};
