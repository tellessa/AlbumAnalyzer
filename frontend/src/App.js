import {useState, useEffect} from 'react';
import './App.css';

function App() {

  const [movies, setMovies] = useState([])
  useEffect (() => {
    setMovies([
      {
        name:'Billions',
        genre: 'Drama',
        starring: 'Damian Lewis, Paul Giamatt',
      },
      {
        name:'Sarafina',
        genre: 'drama',
        starring: 'Leleti Khumalo',
      },

    ])
  }, [])
  return (
    <div className="App">
      {/* const {movies} = movies */}
      {movies.map((movie, index) => {
        return(
          <div className="movies">
            <h2>Movie name: {movie.name}</h2>
            <h3>Genre: {movie.genre}</h3>
            <h4>Starring: {movie.starring}</h4>
          </div>
        )
      }
      )}
    </div>
  );
};

export default App;