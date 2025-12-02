# Play: Yankee - setup

- hosts: db
  become: true
  vars:
    app_name: "yankee_app"
    retry_count: 5

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/yankee/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/yankee/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure india-task-2 is present
      ansible.builtin.file:
        path: /opt/yankee/india-task-2
        state: directory

    - name: Template india-task-2 config
      ansible.builtin.template:
        src: templates/india-task-2.j2
        dest: /etc/yankee/india-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart yankee service
      ansible.builtin.service:
        name: yankee
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
