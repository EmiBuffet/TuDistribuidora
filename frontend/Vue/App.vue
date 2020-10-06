<template>
    <div>
        <h1>Hola {{ firstName }}</h1>
        <app-prueba></app-prueba>
    </div>
</template>
<script>
import Prueba from './components/Prueba.vue';
export default {
    data() {
        return {
            firstName: 'Lucas'
        }
    },
    components: {
        'app-prueba': Prueba
    }
}
</script>