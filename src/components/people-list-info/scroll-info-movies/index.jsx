import React from 'react';
import ImageListItem from '@mui/material/ImageListItem';
import ImageList from '@mui/material/ImageList';

export default function ScrollInfoMovies({ listInfoPeople }) {
<<<<<<< HEAD

=======
    
>>>>>>> f393bfd59599422952d99ac5209358fb674fd1f3
    if (listInfoPeople) {
        return (
            <ImageList sx={{ width: "75%", height: 250 }} cols={1} rowHeight={211}>
                {listInfoPeople?.known_for.map((item, i) => {
                    return <ImageListItem
                        key={item.id * i + "l"}
                        className="my-4 w-75">
<<<<<<< HEAD
                        <img src={`https://image.tmdb.org/t/p/w500${item?.backdrop_path}`}
=======
                        < img
                            src={`http://image.tmdb.org/t/p/w500${item?.backdrop_path}`}
                            srcSet={`http://image.tmdb.org/t/p/w500${item?.backdrop_path}`}
>>>>>>> f393bfd59599422952d99ac5209358fb674fd1f3
                            className="rounded"
                            style={{ width: "75%", height: "100%", objectFit: "cover" }}
                            alt={item.title}
                            loading="lazy" />
                        <span className="fw-bold" style={{ fontSize: "14px" }}>
                            {item.title}
                            {item.name}
                        </span>
                        <span className="fw-light" style={{ fontSize: "12px" }}>
                            {item.release_date}
                        </span>
                    </ImageListItem>
                })
                }
            </ImageList>
        );
    };
}