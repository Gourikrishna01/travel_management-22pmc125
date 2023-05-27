const packageDropdown = document.getElementById('package');
packageDropdown.addEventListener('change', updatePackageDetails);

function updatePackageDetails() {
  // Get the selected package ID
  const packageId = packageDropdown.value;

  // Make an AJAX request to fetch the package details
  fetch(`/packages/${packageId}`)
    .then(response => response.json())
    .then(data => {
      // Update the package details section of the page
      const packageDetails = document.getElementById('package-details');
      packageDetails.innerHTML = `
        <p><strong>Price:</strong> ${data.price}</p>
        <p><strong>Description:</strong> ${data.description}</p>
      `;
    });
}