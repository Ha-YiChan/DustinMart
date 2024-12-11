const productModal = document.getElementById('productInfoModal')
if (productModal) {
    productModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-* attributes
    const title = button.getAttribute('data-title')
    const description = button.getAttribute('data-description')
    // If necessary, you could initiate an Ajax request here
    // and then do the updating in a callback.

    // Update the modal's content.
    const modalTitle = productModal.querySelector('.modal-title')
    const modalBodyP = productModal.querySelector('#prodDesc')

    modalTitle.textContent = title;
    modalBodyP.textContent = description;
  })
}