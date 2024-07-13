import React,{useState,useEffect} from "react"
import api from './api'

function App() {
    const [stocks, setStocks] = useState([]);
    const [formData, setFormData] = useState({
        item_id: '',
        name: '',
        price: '',
        quantity: '',
        category: '',
        date:''
    });

    const fetchStocks = async () => {
        const response = await api.get('/stocks/get_stocks/');
        setStocks(response.data);
    };

    useEffect(() => {
        fetchStocks();
    }, []);

    const handleInputChange = (event) => {
        const value = event.target.type === "checkbox" ? event.target.checked : event.target.value;
        setFormData({
            ...formData,
            [event.target.name]: value,
        });
    };

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        await api.post('/stocks/add_stocks/', formData);
        fetchStocks();
        setFormData({
            item_id: '',
            name: '',
            price: '',
            quantity: '',
            category: '',
            date:''
        });
    };

    return (
        <div>
            <nav className="navbar navbar-dark bg-primary">
                <div className='container-fluid'>
                    <a className='navbar-brand' href="/">
                        Inventory Management App
                    </a>
                </div>
            </nav>


            <div className="container">
                <form onSubmit={handleFormSubmit}>
                    <div className="mb-3 mt-3">
                        <label htmlFor='item_id' className='form-label'>
                            Item Id
                        </label>
                        <input type='text' className='form-control' id='item_id' name='item_id' onChange={handleInputChange} value={formData.item_id} />
                    </div>

                    <div className="mb-3">
                        <label htmlFor='name' className='form-label'>
                            Item Name
                        </label>
                        <input type='text' className='form-control' id='name' name='name' onChange={handleInputChange} value={formData.name} />
                    </div>

                    <div className="mb-3">
                        <label htmlFor='price' className='form-label'>
                            Price
                        </label>
                        <input type='text' className='form-control' id='price' name='price' onChange={handleInputChange} value={formData.price} />
                    </div>

                    <div className="mb-3">
                        <label htmlFor='quantity' className='form-label'>
                            Quantity
                        </label>
                        <input type='text' className='form-control' id='quantity' name='quantity' onChange={handleInputChange} value={formData.quantity} />
                    </div>

                    <div className="mb-3">
                        <label htmlFor='category' className='form-label'>
                            Category
                        </label>
                        <input type='text' className='form-control' id='category' name='category' onChange={handleInputChange} value={formData.category} />
                    </div>
                    <div className='mb-3 mt-3'>
                        <label htmlFor='date' className='form-label'>
                            Date
                        </label>
                        <input type='text' className='form-control' id='date' name='date' onChange={handleInputChange} value={formData.date}/>
                    </div>
                    <button type='submit' className='btn btn-primary'>
                        Submit
                    </button>
                </form>
                <table className='table table-striped table-borderd table-hover'>
                    <thead>
                        <tr>
                            <th>Item Id</th>
                            <th>Item Name</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Category</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {stocks.map((stocks) =>(
                            <tr key={stocks.id}>
                                <td>{stocks.item_id}</td>
                                <td>{stocks.name}</td>
                                <td>{stocks.price}</td>
                                <td>{stocks.quantity}</td>
                                <td>{stocks.category}</td>
                                <td>{stocks.date}</td>
                            </tr>
                        ))}
                    </tbody>
                    </table>
            </div>
        </div>
    );
}

export default App;
