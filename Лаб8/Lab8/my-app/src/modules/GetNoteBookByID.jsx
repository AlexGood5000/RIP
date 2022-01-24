const GetNoteBookByID = async (id = 0) => {
    return await fetch(`http://localhost:8000/notebooks/${id}/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetNoteBookByID;