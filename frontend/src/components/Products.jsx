import React, { useState, useEffect } from "react";

export const Products = ({ access_token }) => {
  const count = React.useRef(0);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (access_token) {
        try {
          const response = await fetch("http://127.0.0.1:8000/api/products", {
            headers: {
              Authorization: `Bearer ${access_token}`,
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
        console.log("JWT inside useEffect", access_token);
      }
    };

    fetchData();
    count.current = count.current + 1;
    console.log("products", products);
  }, [access_token]);

  return (
    <div>
      {products && (
        <>
          {products.map((item, index) => (
            <div key={index}>
              <p>{item.name}</p>
              <img src={item.image} alt="item.name" />
            </div>
          ))}
        </>
      )}
      <h1>Render Count: {count.current}</h1>
    </div>
  );
};
