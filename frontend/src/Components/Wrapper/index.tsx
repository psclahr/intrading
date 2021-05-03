import { makeStyles } from '@material-ui/core';
import React from 'react'
import Header from './Header';

const useStyles = makeStyles(() => ({
    wrapper: {
        display: 'grid',    
    },
    main: {}
}))

const Wrapper: React.FC = (props) => {
    const classes = useStyles()

    return (
        <div className={classes.wrapper}>
            <Header/>
            <div className={classes.main}>
                {props.children}
            </div> 
        </div>
    )
}

export default Wrapper;
