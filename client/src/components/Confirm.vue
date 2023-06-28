<template>
    <div>
        <div class="alert alert-warning alert-dismissable fade show" role="alert">{{ message }}<button type="button" class="close" data-dismiss="alert" aria-label="Close"></button>
            
</div>
        <br/>
    </div>
</template>
<script>
export default {
    props: ['message'],
};
</script>