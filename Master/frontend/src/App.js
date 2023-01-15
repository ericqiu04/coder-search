import { useState } from 'react'
import Axios from 'axios'
import Cookies from 'react-cookies';


function App() {

  const [inputValue, setInputValue] = useState('')
  
  const data = new FormData()
  data.append("input", inputValue)


  const handleSubmit = (event) => {
    event.preventDefault();
    Axios.post('/submit-input/', {input_data: inputValue}, {
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.load('csrftoken')
      }
    })
      .then(response => {
        console.log(inputValue)
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }



  return (
    <div className="flex flex-col justify-center h-screen dark:bg-gray-700">
      <div className="text-center" >
        <h1 className="sm:text-4xl dark:text-white font-jetbrains z-0 text-lg">
          <span>&#60;</span> Coder <span>&#62;</span> Search
        </h1>
      </div>
      <form onSubmit={handleSubmit} method="post">

        <div className="mx-auto mt-4 mb-16 relative w-4/6 z-[100]" >

          <div className="absolute inset-y-0 1/2 left-0 flex items-center pl-3 pointer-events-none">
            <button type="submit">
              <svg
                aria-hidden="true"
                className="w-5 h-5 text-gray-500 dark:text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                ></path>
              </svg>
            </button>

          </div>
          <input
            type="search"
            id="default-search"
            className="text-xl font-jetbrains sm:text-base w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Search Code..."
            value={inputValue}
            onChange={event => setInputValue(event.target.value)}
            required
          />
        </div>
      </form>
      <h1>
        {inputValue}
      </h1>
    </div>
  );
}

export default App;
