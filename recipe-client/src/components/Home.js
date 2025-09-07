import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    axios.get('/api/categories/')
      .then(response => {
        setCategories(response.data);
      });
  }, []);

  return (
    <div>
      <h1>Рецепты</h1>
      <ul>
        {categories.map(category => (
          <li key={category.id}>
            <Link to={`/category/${category.id}`}>{category.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
