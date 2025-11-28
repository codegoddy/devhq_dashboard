/** @format */

import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import axios from "axios";

export default function Emails() {
  const [recipients, setRecipients] = useState("");
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [message, setMessage] = useState("");
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/login");
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    try {
      await axios.post(
        "http://localhost:8000/emails/send",
        {
          recipients: recipients.split(",").map((r) => r.trim()),
          subject,
          body,
        },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      setMessage("Email sent successfully");
      setRecipients("");
      setSubject("");
      setBody("");
    } catch (err) {
      setMessage("Failed to send email");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <div className="flex-shrink-0 flex items-center">
                <h1 className="text-xl font-bold">DevHQ Dashboard - Emails</h1>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <a
                href="/dashboard"
                className="text-gray-700 hover:text-gray-900"
              >
                Dashboard
              </a>
              <a href="/users" className="text-gray-700 hover:text-gray-900">
                Users
              </a>
              <button
                onClick={() => {
                  localStorage.removeItem("token");
                  router.push("/login");
                }}
                className="text-gray-700 hover:text-gray-900"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <h2 className="text-2xl font-bold mb-6">Send Email</h2>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label
                htmlFor="recipients"
                className="block text-sm font-medium text-gray-700"
              >
                Recipients (comma separated)
              </label>
              <input
                type="text"
                id="recipients"
                value={recipients}
                onChange={(e) => setRecipients(e.target.value)}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                required
              />
            </div>
            <div>
              <label
                htmlFor="subject"
                className="block text-sm font-medium text-gray-700"
              >
                Subject
              </label>
              <input
                type="text"
                id="subject"
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                required
              />
            </div>
            <div>
              <label
                htmlFor="body"
                className="block text-sm font-medium text-gray-700"
              >
                Body
              </label>
              <textarea
                id="body"
                rows="4"
                value={body}
                onChange={(e) => setBody(e.target.value)}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                required
              />
            </div>
            <button
              type="submit"
              className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Send Email
            </button>
          </form>
          {message && <p className="mt-4 text-sm text-gray-600">{message}</p>}
        </div>
      </main>
    </div>
  );
}
