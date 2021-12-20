FROM alpine:latest AS mybuild
RUN set -ex && apk --no-cache --update add build-base 
WORKDIR /src
COPY hello.cpp ./
# compile with -static option for static binary
RUN g++ -static hello.cpp -o hello
# now just take the binary from build stage
FROM alpine:latest
# create a user; this user will apply to all RUN, ENTRYPOINT and CMD after this line
USER nobody
# add chmod to copy because if we do it on separate RUN it will increase total size
# we also set file ownership to 'nobody' user as we are giving execute permission to owner only
COPY --from=mybuild --chown=nobody --chmod=744 /src/hello /myapp/
# RUN commend create a layer and copies the file to perm so avoid it
# RUN chmod +x /myapp/hello
CMD [ "/myapp/hello" ]
