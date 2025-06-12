---
marp: true
theme: summary
math: mathjax
---
# Web application security

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

Web applications are the current paradigm for software delivery. They are built on top of HTTP which is a stateless protocol. The emulation of a state is implemented through additional mechanisms.

The golden rule of web application security is that the **client is never trustworthy**. We need to **validate** and **check carefully** anything that is sent to us.

**Filtering** untrusted data is hard.
This is a standard validation sequence:
1. **Allowlisting**: only allowing through what we expect.
2. **Blocklisting**: discard known-bad stuff.
3. **Escaping**: transform special characters into something else which is less dangerous.

As a basic rule: _allowlisting_ is safer than _blocklisting_.

## Cross Site Scripting (XSS)

Suppose to  have a simple blog app where anybody can post comments by filling a simple text field. The comment are displayed back to next visitors.
If we <u>do not apply any filter to what is inserted</u>, an attacker could type:
```
<script>
    alert('JavaScript Executed');
</script>
```
Then, a pop-up would appear on the next visitors' screen.
This is called **Cross Site Scripting** (**XSS**).

**XSS** is a vulnerability by means of which **client-side code** can be injected in a page.
There are three types of XSS:
- Stored XSS.
- Reflected XSS.
- Dom-based XSS.

### Stored (a.k.a. persistent) XSS

In **stored XSS**, the attacker input is stored on the target server in a database (e.g., in a _message forum_, _visitor log_, _comment field_).
Then, a victim retrieves the stored malicious code from the web application <u>without that data being made safe to render in the browser</u>.

---

### Reflected (a.k.a. non-persistent) XSS

In **reflected XSS**, the client input (i.e., the request payload) is returned to the client by the web application in a response (e.g., an error message, a search result). The response includes some or all of the input provided in the request **without being stored** and **made sage to render** in the browser.

An attacker could craft a malicious request into a link and send it to a victim.

### DOM-based XSS

In **DOM-based XSS**, the user input never leaves the victim's browser: the malicious payload is directly executed by a client-side script (e.g., a script that modifies/updates the DOM in-memory representation of a page including forms).

### The Same Origin Policy (SOP)

The **Same Origin Policy** (**SOP**) states that all client-side code (e.g., JavaScript), loaded from origin $A$ should only be able to access data from origin $A$. Modern web has "blurry" boundaries, like **Cross-origin resource sharing** (**CORS**).

### The power of XSS

XSS can be used for:
- Cookie theft or session hijack.
- Manipulation of a session and execution of a fraudulent transaction.
- Snooping on private information.
- **Drive by Download**.
- Effectively bypasses the same-origin policy.

The only effective countermeasure against XSS is to design an allowlist with alphanumeric characters plus punctuation, including < and > and other special characters, and then escape < and > with their equivalent HTML safe: "\&gt;", "\&lt;".
Another useful example: "&", becomes "\&amp".

### Content Security Policy (CSP)

The **Content Security Policy** (**CSP**) is a W3C specification to inform the browser on what should be trusted, and what shouldn't. You can think of it as the same-origin policy, but with flexible and more expressive policies. Technically, it is implemented as a set of directives sent by the server to the client in the form of HTTP response headers.
Many directives are available, for instance:
- `script-src`: load client code only from listed origins;
- `form-action`: lists valid endpoints for submission;
- `frame-ancestors`: lists sources that can embed the current page as frames and applets.

---

- `img-src`: defines the origins from which images can be loaded.
- `style-src`: as `script-src` but for stylesheets.

Being this just specification, the actual behavior is up to the browser implementation.

CSP is a great idea, but it slowly gaining traction. There is a tradeoff: strict policies break functionalities and relaxed policies can be bypassed.
There are also some practical barriers and challenges: writing policies is mainly a manual process; something can be automated, but not all.
Keeping policies up to date is difficult. Furthermore there are browser extensions that inject new code.

## SQL injection

Consider now a web application with a simple login page composed of a form with two fields: `txtUser` and `txtPassword`.
The values put in the fields are used to perform a SQL query:
```
SELECT * FROM Users
WHERE username='{txtUser}'
AND password='{txtPassword}';
```
If the query returns at least one row, the user is granted access.
What happens if we put in input `txtUser = mariorossi' ;--`. Remember that `--` is the syntax to comment in SQL. Then, the query returns at least one row if the user exists: we don't need to know the password.
We can get access even if we don't know the name of a valid user. Simply write `txtUser = ' OR '1'='1' ;--`. This quey gets executed, and the second part of the OR is always true: it returns all words, which is reasonably more than one, and our attacker is granted access.

A naive countermeasure would be at least to blocklist or escape "' ;--".

### Retrieving results and `UNIONS`

Let's consider **another example**. Suppose we are running the following query <u>that displays the results</u>:
```
SELECT name, phone, address FROM Users
WHERE Id='{userinput}';
```

If `userinput` is not filtered, we can do:
```
SELECT name, phone, address FROM Users
WHERE Id='' OR '1'='1' ;--';
```
which will display <u>all the contents of that table</u>.

Another possible injection is:
```
SELECT name, phone, address FROM Users
WHERE Id='' UNION ALL SELECT
name, creditCardNumber, CCV2 FROM
CreditCardTable; --';
```

---

This will show the content of a different table. **Warning**: <u>it will work only if the number and data types of the columns are the same</u>.

### Injections on Inserts

Consider **another example**: a simple app that stores exam results according to the following schema:
```
CREATE TABLE users (
    id INTEGER,
    user VARCHAR(128),
    password VARCHAR(128),
    result VARCHAR,
    PRIMARY KEY (id)
)
```
```
CREATE TABLE results (
    id INTEGER,
    username VARCHAR(128),
    grade VARCHAR,
    PRIMARY KEY (id)
)
```
The app runs queries like the following to insert data:
```
INSERT INTO result VALUES (NULL, 'username', 'grade');
```
A possible injection is:
```
INSERT INTO results VALUES (NULL, 'mariorossi', '30L'); --', 18);
```
Furthermore, INSERT INTO allows multiple tuples as values:
```
INSERT INTO results VALUES (NULL, 'mariorossi', '30L'),
(NULL, 'marcobianchi', '30L'); --', 18);
```
It is also possible to use **subqueries**:
```
INSERT INTO results VALUES (NULL, 'mariorossi',
(SELECT passwrod from USERS where user='admin')); --', '18');
```
Observe that <u>you will need to retrieve this data</u> if it's stored somewhere or try a <u>blind injection</u>.

### Blind injections

Some SQL queries, such as the login query we saw, do NOT display returned values. Rather they do or do not do stuff, based on the return value. We cannot use them to directly display data, but we can play with their behavior to infer data.
There are known as "blind" SQL injections.

### Possible countermeasures

Input sanitization is a way of making the exploitation more difficult. If the language allows it, you can use prepared statements (parametric queries), instead of building "query strings".

---

Furthermore, you should set limitations on query privileges: different users can execute different types of queries on different tables/DBs.

## Recap on Code Injection Problems

Code Injection Problems happen when we need to mix code and data due to functional requirements.

## Cross-Site Request Forgery (CSRF)

A **Cross-Site Request Forgery** (**CSRF**) forces a user to execute **unwanted actions** (**state-changing actions**) on a web application in which he or she is **currently authenticated** with ambient credentials (e.g. with cookies).

The key concepts are the following. Cookies are used for session management.
All the requests originating by the browser come with the user's cookies (they are sent automatically for every request). Malicious requests are routed to the vulnerable web application to the victim's browser.
Websites cannot distinguish if the requests coming from authenticated users have been originated by an explicit user interaction or not.

To mitigate the problem, you should use a **CSRF token**, i.e., a random challenge token associated to user's session and regenerated at each request. It is sent to the server and then compared against the stored token. Sever-side operations are allowed only if there is a match. It should not be stored in cookies.

Another idea is to do not send session cookies at all for requests originating from different websites. Websites specify this behavior when setting a cookie, using the `SameSite` attribute: `SameSite=strict` doesn't allow to send cookies for any cross-site usage; `SameSite=lax` allows to send cookies for cross-domain navigation only.
