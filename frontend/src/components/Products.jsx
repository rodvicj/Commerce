import { useState, useEffect } from "react";

const Products = ({name}) => {
  const [list, setList] = useState([
    {
      name: "test123",
      image: "testImages",
    },
  ]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:8000/api/products");
      const json = await response.json();
      console.log(json);
      setList(json.results);
    };

    fetchData();
  }, []);

  return (
    <div>
      <p>Hello {name}</p>
      {list.map((item, index) => {
        return (
          <div key={index}>
            <p>{item.name}</p>
            <img src={item.image} alt="item.name" />
          </div>
        );
      })}
    </div>
  );
};

export default Products;
