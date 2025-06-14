---
marp: true
theme: summary
math: mathjax
---
# Network security protocols

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

The internet protocols we tackled so far **lack** of **authentication** and **confidentiality**. 
Two protocols were developed to handle this problem:
- The **HTTP over SSL** (**Secure Socket Layer**), a.k.a. **HTTPS**: it provides communication confidentiality and integrity, and mutual authentication.
- The **SET** (**Secure Electronic Transaction**) protocol: it guarantees on data usage and transaction security enforcement.

## TLS

SSL has been updated into its more secure version **TLS**. It enforces confidentiality and integrity of the communications, server authentication, and (optionally) client authentication. It uses both symmetric and asymmetric cryptography for performance reasons.

TLS is designed to be flexible wrt to technical evolution. Clients and servers may use different _suites_ of algorithms for different functions:
- a key exchange/key encapsulation algorithm;
- a symmetric encryption algorithm;
- a digital signature algorithm;
- a hash function (for symmetric key derivation).

During the **TLS handshake**, cipher suites are compared to agree on shared algorithms in order of preference. THe standard mandates the implementation of a minimal cipher set.

Once the client sends its cipher suite plus random data, the server responds with the cipher selection plus other random data and the server certificate. The server certificate is validated as we have seen in the "_Introduction to Cryptography_" set of notes.

Afterwards, the client sends a pre-master secret, encrypted with the server public key, which is signed with the client private key.

A shared secret is computed from pre-master secret, client random data and server random data. The communication now happens over an encrypted channel.

Observe that TLS is resistant to MITM attacks by design.

The **advantages** of TLS are that it protects transmissions, guaranteeing confidentiality and integrity and it ensures authentication of the server and (optionally) of the client.

---

The **disadvantages** are that it offers no protection before or after the transmission on the server or on the client and it relies on the PKI. Finally, it is not foolproof.

### Overcoming TLS limitations
#### HTTP Strict Transport Security (HSTS)

**HTTP Strict Transport Security** (**HSTS**) is an HTTP header to tell the browser to always connect to a certain domain using HTTPS.

#### HTTP Public Key Pinning (HPKP)

**HTTP Public Key Pinning** (**HPKP**) is an HTTP header to tell the browser to "pin" a specific certificate or a specific CA. The browser will refuse certificates from different CAs for that origin. It allows to defend against trust certificate mis-issuance.

## SET

SET is the result of a joint effort of VISA and MasterCard. The idea is to protect _transactions_ , not _connection_. The approach is the following: the **cardholder** sends the **order of goods** to the **merchant only**, the **payment data** to the **payment gateway** only. It uses the concept of a dual signature. The two data are hashed individually, the resulting digests are concatenated and hashed again. The result is signed with the cardholder private key.
The hash of the payment data is sent to the merchant, while the hash of the order of goods is sent to the payment gateway, so that both can verify the integrity without needing to know data outside of their competences.

The issue of SET is that it requires a certificate also for the cardholder: a pre-registration of the cardholder is needed.
