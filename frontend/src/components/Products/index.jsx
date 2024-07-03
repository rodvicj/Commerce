import React, { useState, useEffect } from "react";

import "./styles.css";

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
    <div className="products__container">
      {products && (
        <>
          {products.map((item) => (
            <div className="products__container-wrapper" key={item.id}>
              <h1 className="products__item-title">{item.name}</h1>
              <img
                className="products__image"
                src={item.image}
                alt={item.name}
              />
              <h2 className="products__description">{item.description}</h2>
            </div>
          ))}
        </>
      )}
      <h1 style={{ color: "red", padding: "1.5em" }}>
        Render Count: {count.current}
      </h1>
    </div>
  );
};

export default Products;

// TODO: style products__container as flex as default
