import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetNoteBooks from "../modules/GetNoteBooks";

function NoteBookListPage() {

    const [notebooks, setNoteBooks] = useState([]);

    const handleNoteBooksList = async () => {
        const results = await GetNoteBooks();
        await setNoteBooks(results);
    }

    useEffect(() => {
        handleNoteBooksList();
    }, []);


    return (
        <div>
            <Header/>
            <ul className="fs-4">
                {notebooks.map((notebook) => {
                    return (<li key={notebook.id}><Link to={"/notebooks/" + notebook.id.toString()}
                                                     className="text-decoration-none link-dark">
                        {notebook.name}</Link></li>);

                })}
            </ul>
            <Footer/>
        </div>
    );
}

export default NoteBookListPage;