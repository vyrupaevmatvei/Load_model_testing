AUTH=$(echo -n "${REGISTRY_USER}:${REGISTRY_PASSWORD}" | base64)
cat << EOF > config.json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "${AUTH}"
        }
    }
}
EOF