import axios from "axios";
import { useEffect } from "react";

useEffect(() => {
  const fetchTodos = async () => {
    const response = await axios.get("http://localhost:8000/api/todos/");
    console.log("response", response);
  };
  fetchTodos();
}, []);
