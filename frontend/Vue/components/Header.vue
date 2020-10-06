<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="https://bulma.io">
                <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
            </a>

            <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
                data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item" exact>Inicio</router-link>

                <a class="navbar-item">
                    Productos
                </a>

                <a class="navbar-item">
                    <span class="icon">
                        <i class="fas fa-columns"></i>
                    </span>
                    <span>Dashboard</span>
                </a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link    to="/login" 
                                        class="button is-primary"
                                        active-class="is-active"
                                        exact>Ingresar</router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {

    }
</script>