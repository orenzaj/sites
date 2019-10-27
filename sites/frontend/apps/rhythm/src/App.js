import React, { useState, useEffect } from "react";
import {
    AppContainer,
    ListContainer,
} from "./styled/Components";
import { makeStyles } from '@material-ui/core/styles';
import { Fab } from '@material-ui/core';
import { Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon, Navigation as NavigationIcon } from '@material-ui/icons';

const useStyles = makeStyles(theme => ({
  fab: {
    margin: theme.spacing(1),
  },
  extendedIcon: {
    marginRight: theme.spacing(1),
  },
}));

const App = () => {
    const [songs, setSongs] = useState([]);
    const [artists, setArtists] = useState([]);
    const [sounds, setSounds] = useState([]);
    const [hasErrors, setErrors] = useState(false);
    const classes = useStyles();

    useEffect(() => {
        async function fetchModel(resource, setterFunc){
            const response = await fetch(`http://localhost:8081/api/${resource}/`);
            response
                .json()
                .then(response => setterFunc(response))
                .catch(error => setErrors(error))
            ;
        }
        fetchModel("songs", setSongs);
        fetchModel("artists", setArtists);
        fetchModel("sounds", setSounds);
    }, []);

    return (
        <AppContainer className="app_container">
            <ListContainer className="songs_container">
                <Fab color="primary" aria-label="add" className={classes.fab}>
                    <AddIcon/>
                </Fab>
                {songs.map(song => {
                    return (
                        <div key={song.title}>
                            {song.title}
                            <Fab color="primary" aria-label="edit" className={classes.fab}>
                                <EditIcon/>
                            </Fab>
                            <Fab color="primary" aria-label="delete" className={classes.fab}>
                                <DeleteIcon/>
                            </Fab>
                        </div>
                    )
                })}
            </ListContainer>
            <ListContainer className="artists_container">
                <Fab color="primary" aria-label="add" className={classes.fab}>
                    <AddIcon/>
                </Fab>
                {artists.map(artist => {
                    return (
                        <div key={artist.name}>
                            {artist.name}
                            <Fab color="primary" aria-label="edit" className={classes.fab}>
                                <EditIcon/>
                            </Fab>
                            <Fab color="primary" aria-label="delete" className={classes.fab}>
                                <DeleteIcon/>
                            </Fab>
                        </div>
                    )
                })}
            </ListContainer>
            <ListContainer className="sounds_container">
                <Fab color="primary" aria-label="add" className={classes.fab}>
                    <AddIcon/>
                </Fab>
                {sounds.map(sound => {
                    return (
                        <div key={sound.name}>
                            {sound.name}
                            <Fab color="primary" aria-label="edit" className={classes.fab}>
                                <EditIcon/>
                            </Fab>
                            <Fab color="primary" aria-label="delete" className={classes.fab}>
                                <DeleteIcon/>
                            </Fab>
                        </div>
                    )
                })}
            </ListContainer>
        </AppContainer>
    );
};

export default App;
