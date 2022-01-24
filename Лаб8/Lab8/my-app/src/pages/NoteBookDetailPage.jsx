import React, {useEffect, useState} from "react";
import {useParams} from "react-router";
import {Table} from "react-bootstrap";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetNoteBookByID from "../modules/GetNoteBookByID";

function NoteBookDetailPage() {
    const id = useParams().id;
    console.log(id);

    const [notebook, setNoteBook] = useState({});

    const handleNoteBook = async () => {
        const result = await GetNoteBookByID(id);
        await setNoteBook(result);
    }

    useEffect(() => {
        handleNoteBook();}, []);

    useEffect(() => {
        console.log(notebook);}, [notebook])

    return (
        <div>
            <Header/>
            <Table striped bordered size="sm" className="fs-4">
                <tbody>
                <tr>
                    <td className="mx-2">Производитель</td>
                    <td className="mx-2">{notebook.manufacturer}</td>
                </tr>
                <tr>
                    <td className="mx-2">Модель</td>
                    <td className="mx-2">{notebook.name}</td>
                </tr>
                <tr>
                    <td className="mx-2">Дисплей</td>
                    <td className="mx-2">{notebook.display}</td>
                </tr>
                <tr>
                    <td className="mx-2">Операционная система</td>
                    <td className="mx-2">{notebook.os}</td>
                </tr>
                </tbody>
            </Table>
            <Footer/>
        </div>
    );
}

export default NoteBookDetailPage;