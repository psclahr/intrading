import React from 'react'
import { AppBar, Toolbar, IconButton, Button, Typography, makeStyles } from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles(() => ({
    menuButton: {
        marginRight: '10px',
    },
    title: {
        flexGrow: 1,
    },
}))

const Header: React.FC = () => {
    const classes = useStyles()

    return (
        <AppBar position="static">
            <Toolbar>
                <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                    <MenuIcon/>
                </IconButton>
                <Typography variant="h6" className={classes.title}>
                Intrading
                </Typography>
                <Button color="inherit">Login</Button>
            </Toolbar>
        </AppBar>
    )
}

export default Header
