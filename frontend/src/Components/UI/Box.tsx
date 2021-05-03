import classes from '*.module.css'
import { Card, makeStyles } from '@material-ui/core'
import React from 'react'

const useStyles = makeStyles(() => ({
    card: {
        margin: '3rem'
    }
}))

const Box: React.FC = (props) => {
    const classes = useStyles()

    return (
        <Card className={classes.card}>
            {props.children}
        </Card>
    )
}

export default Box
