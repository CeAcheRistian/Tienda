const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    notificacionSwal.fire({
        titleText: titleText,
        text: text,
        icon: icon,
        confirmButtonText: confirmButtonText
    })
}