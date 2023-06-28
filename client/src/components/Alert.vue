<template>
    <div>
        <div class="alert alert-success" role="alert">{{ message }}
            <!-- <button type="button" class="btn-close" data-dismiss="alert" aria-label="Close"></button> -->
</div>
        <br/>
    </div>
</template>
<script>
export default {
    props: ['message'],
};
</script>