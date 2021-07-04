import React from "react"
import 'bootstrap/dist/css/bootstrap.css'
import axios from "axios"
import debounce from 'lodash/debounce'

class SearchResultList extends React.Component{
    constructor(props){
        super(props);
        this.state = {}
    }
    render(){
        return (
            this.props.books.map((book, i) => {
                return (
                    <tr key={book.id} className="text-center">
                        <td>{book.id}</td>
                        <td>{book.title}</td>
                        <td>{book.author}</td>
                        <td>{book.price}</td>
                    </tr>
                )
            })
        )
    }
}

class SearchResult extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            books: null,
            isLoaded: false,
            error: null
        }
    }
    getData(){
        console.info(123)
        const _this = this;
        axios.get('/bookstore/api/v1/book/'+this.props.searchText)
        .then(function (response) {
            _this.setState({
                books: response.data,
                isLoaded: true
            });
            console.log(_this.state.books);
        })
        .catch(function (error) {
            _this.setState({
                isLoaded: false,
                error: error
            })
        })
    }
    componentWillUpdate(){
        this.getData()
    }
    render() {
        if(!this.state.isLoaded){
            return <div>Loading</div>
        } else{
            if (!this.state.books)
                return <div>空空如也</div>
            return (
                <table className="table table-bordered">
                    <thead>
                        <tr>
                            <th className="text-center">id</th>
                            <th className="text-center">书名</th>
                            <th className="text-center">作者</th>
                            <th className="text-center">价格/￥</th>
                        </tr>
                    </thead>
                    <tbody>
                        <SearchResultList books={this.state.books} />
                    </tbody>
                </table>
            )
        }
    }
}

class SearchInput extends React.Component {
    constructor(props){
        super(props);
        this.handleSearchTextInputChange = this.handleSearchTextInputChange.bind(this);
        this.state = {}
    }

    handleSearchTextInputChange(e){
        this.props.onSearchTextInput(e.target.value);
    }
    render() {
        return (
            <form>
                <input
                    type="text"
                    placeholder="Search..."
                    value={this.props.searchText}
                    onChange={this.handleSearchTextInputChange} 
                />
            </form>
        )
    }
}

class SearchBox extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            searchText: 'index'
        }

        this.handleSearchTextInput = this.handleSearchTextInput.bind(this)
        // this.handleSearchTextInput = debounce(this.handleSearchTextInput, 200)
    }
    handleSearchTextInput(searchText) {
        this.setState({
            searchText: searchText
        })
    }
    render() {
        return (
            <div className="">
                <SearchInput
                    searchText={this.state.searchText}
                    onSearchTextInput={this.handleSearchTextInput} 
                />
                <SearchResult 
                    searchText={ this.state.searchText }
                />
            </div>
        )
    }
}

export default SearchBox;